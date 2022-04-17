# create the credentials
AdminTask.createAuthDataEntry(
    '['
    '-alias ORACLE_DEMO '
    '-user DEMO '
    '-password DEMO '
    '-description '
    '"ORACLE DEMO" '
    ']'
)

# create the jdbcProvider
jdbcProvider = AdminTask.createJDBCProvider(
    '['
    '-scope Node=DefaultNode01,Server=server1 '
    '-databaseType Oracle '
    '-providerType "Oracle JDBC Driver" '
    '-implementationType "XA data source" '
    '-name "Oracle JDBC Driver (XA)" '
    '-description "Oracle JDBC Driver (XA)" '
    '-classpath [/work/mount/jdbc/oracle/ojdbc8.jar ] '
    '-nativePath "" '
    ']'
)

# create the datasource
AdminTask.createDatasource(
    jdbcProvider,
    '['
    '-name ORACLE_DEMO '
    '-jndiName default/ds '
    '-dataStoreHelperClassName com.ibm.websphere.rsadapter.Oracle11gDataStoreHelper '
    '-containerManagedPersistence true '
    '-componentManagedAuthenticationAlias DefaultNode01/ORACLE_DEMO '
    '-xaRecoveryAuthAlias DefaultNode01/ORACLE_DEMO '
    '-configureResourceProperties [[URL java.lang.String jdbc:oracle:thin:@//oracle:1521/XEPDB1]]'
    ']'
)

AdminConfig.save()