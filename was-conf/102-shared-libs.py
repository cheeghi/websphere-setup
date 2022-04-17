AdminConfig.create(
    'Library',
    AdminConfig.getid('/Cell:DefaultCell01/Node:DefaultNode01/Server:server1/'),
    '['
    '[nativePath ""] '
    '[name "DEFAULT_SHARED_LIB"] '
    '[isolatedClassLoader false] '
    '[description "default shared lib"] '
    '[classPath "/work/mount/shared_lib/default"]'
    ']'
)

AdminConfig.save()