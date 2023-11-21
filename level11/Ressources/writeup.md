On this exercise there is a lua file describing how is working a server curently running.

#!/usr/bin/env lua
local socket = require("socket")
local server = assert(socket.bind("127.0.0.1", 5151))

function hash(pass)
  prog = io.popen("echo "..pass.." | sha1sum", "r")
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

it is listening at localhost 127.0.0.1 with the port 5151
For every connection it display a message asking for a password.
After capturing the password, it exeucte a function starting by "io.popen("echo "..pass.." | sha1sum", "r")"

io.popen is a function returning a result of a command send as string executed by the system.
pass is our variable previously send and captured.
.. operator, in lua is used to concatenate strings.

Ive found the flag by sending the password "& getflag > /tmp/flag" so the bash is executing : "echo & getflag > /tmp/flag | sha1sum"

The flag is then present at /tmp/flag