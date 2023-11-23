In this exercise, there is a Lua file describing how a currently running server works:

```lua
#!/usr/bin/env lua
local socket = require("socket")
local server = assert(socket.bind("127.0.0.1", 5151))

function hash(pass)
  prog = io.popen("echo " .. pass .. " | sha1sum", "r")
  data = prog:read("*all")
  prog:close()

  data = string.sub(data, 1, 40)

  return data
end

while 1 do
  local client = server:accept()
  client:send("Password: ")
  client:settimeout(60)
  local l, err = client:receive()
  if not err then
      print("trying " .. l)
      local h = hash(l)

      if h ~= "f05d1d066fb246efe0c6f7d095f909a7a0cf34a0" then
          client:send("Erf nope..\n");
      else
          client:send("Gz you dumb*\n")
      end
  end

  client:close()
end
```

It is listening on localhost (127.0.0.1) on port 5151. For every connection, it displays a message asking for a password. After capturing the password, it executes a function starting with `io.popen("echo " .. pass .. " | sha1sum", "r")`.

The `io.popen` function returns the result of a command sent as a string and executed by the system. Here, `pass` is the variable previously sent and captured. The `..` operator in Lua is used to concatenate strings.

The flag was found by sending the password "& getflag > /tmp/flag". This causes the Bash to execute the command "echo & getflag > /tmp/flag | sha1sum". The flag is then present at /tmp/flag.