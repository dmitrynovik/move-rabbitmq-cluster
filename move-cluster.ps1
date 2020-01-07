Param (
    [Parameter(Mandatory=$true)] [uri] $from,
    [string] $fromUser = "admin",
    [string] $fromPassword = "admin",
    [Parameter(Mandatory=$true)] [uri] $to,
    [string] $toUser = "admin",
    [string] $toPassword = "admin"
)

if ($to -eq $from) {
    throw "Cannot move to the same destination: $to"
}

# export definitions
$defs_path = "rabbitmq.definitions.json"
python .\rabbitmqadmin -H $from -u $fromUser -p $fromPassword export $defs_path

# TODO