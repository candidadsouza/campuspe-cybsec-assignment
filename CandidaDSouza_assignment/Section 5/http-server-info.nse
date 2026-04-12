local http = require "http"

description = [[
Shows server info from website
]]

author = "Student"
categories = {"default", "safe"}

-- run only on port 80 or 8080
portrule = function(host, port)
    if port.number == 80 or port.number == 8080 then
        return true
    end
    return false
end

-- main function
action = function(host, port)

    -- send request to homepage
    local response = http.get(host, port, "/")

    if response then

        -- get server name
        local server = response.header.server
        if not server then
            server = "Not found"
        end

        -- get status code
        local status = response.status

        -- get page title
        local title = "Not found"

        if response.body then
            local found_title = response.body:match("<title>(.-)</title>")

            if found_title then
                title = found_title
            end
        end

        -- show results
        return "Server: " .. server ..
               "\nStatus Code: " .. status ..
               "\nPage Title: " .. title
    end

    return "Could not connect"
end
