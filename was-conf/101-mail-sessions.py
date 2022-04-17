AdminConfig.create(
    'MailSession',
    AdminConfig.getid('/Cell:DefaultCell01/Node:DefaultNode01/Server:server1/MailProvider:Built-in Mail Provider/'),
    '['
    '[name "default mail"] '
    '[debug "false"] '
    '[mailStoreUser ""] '
    '[category ""] '
    '[mailTransportHost "mysmtp.domain.com"] '
    '[jndiName "default/wail"] '
    '[mailTransportUser ""] '
    '[mailStorePassword "********"] '
    '[mailStoreHost ""] '
    '[strict "true"] '
    '[description ""] '
    '[mailTransportPassword "********"] '
    '[mailFrom ""] '
    '[mailTransportProtocol "(cells/DefaultCell01/nodes/DefaultNode01/servers/server1|resources.xml#builtin_smtp)"]'
    ']'
)

AdminConfig.save()