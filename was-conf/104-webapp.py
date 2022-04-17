AdminApp.install(
    '/work/webapp-1.0-SNAPSHOT.war',
    '[ '
    '-nopreCompileJSPs '
    '-distributeApp '
    '-nouseMetaDataFromBinary '
    '-nodeployejb '
    '-appname webapp-1_0-SNAPSHOT_war '
    '-createMBeansForResources '
    '-noreloadEnabled '
    '-nodeployws '
    '-validateinstall warn '
    '-noprocessEmbeddedConfig '
    '-filepermission .*\.dll=755#.*\.so=755#.*\.a=755#.*\.sl=755 '
    '-noallowDispatchRemoteInclude '
    '-noallowServiceRemoteInclude '
    '-asyncRequestDispatchType DISABLED '
    '-nouseAutoLink '
    '-noenableClientModule '
    '-clientMode isolated '
    '-novalidateSchema '
    '-contextroot / '
    '-MapResRefToEJB ['
    '[ "Sample Webapp" "" webapp-1.0-SNAPSHOT.war,WEB-INF/web.xml default/ds javax.sql.DataSource default/ds "" "" "" ]'
    '] '
    '-MapModulesToServers ['
    '[ "Sample Webapp" webapp-1.0-SNAPSHOT.war,WEB-INF/web.xml WebSphere:cell=DefaultCell01,node=DefaultNode01,server=server1 ]'
    '] '
    '-MapWebModToVH ['
    '[ "Sample Webapp" webapp-1.0-SNAPSHOT.war,WEB-INF/web.xml default_host ]'
    ']'
    '-MapSharedLibForMod [[ webapp-1_0-SNAPSHOT_war META-INF/application.xml DEFAULT_SHARED_LIB ]] '
    ']'
)

# change class loader order to PARENT_LAST
# deployments = AdminConfig.getid('/Deployment:webapp-1_0-SNAPSHOT_war/')
# deploymentObject = AdminConfig.showAttribute(deployments, 'deployedObject')
# myModules = AdminConfig.showAttribute(deploymentObject, 'modules')
# myModules = myModules[1:len(myModules)-1].split(" ")
# # print myModules
# for module in myModules:
#     if (module.find('WebModuleDeployment')!= -1):
#         AdminConfig.modify(module, [['classloaderMode', 'PARENT_LAST']])

AdminConfig.save()