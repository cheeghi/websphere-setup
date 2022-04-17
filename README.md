## Websphere Setup
Docker Compose that runs and configures a [Webpshere Traditional](https://github.com/WASdev/ci.docker.websphere-traditional) server along with an [Oracle XE](https://github.com/gvenzl/oci-oracle-xe) database. This project aims to provide a skeleton to easily configure and test applications on Webpshere.

## Get started

Clone the project and run `docker-compose up`.

## Websphere

Once the server starts up you can reach the admin console at https://localhost:9043/ibm/console/login.do (login with `wsadmin/wsadmin`), while the webapps are deployed under https://localhost:9443/.

Websphere comes with some pre-configured resources:
* a shared library (named `DEFAULT_SHARED_LIBRARY`)
* an xa oracle jdbc provider and an oracle datasource (jndi `default/ds`) which connects to the oracle xe container
* a sample webapp which connects to the oracle database and references the default shared library

The shared library is mounted on the host folder [/mount](https://github.com/cheeghi/websphere-setup/tree/main/mount), so it's not necessary to rebuild the image each time a file is modified. This folder also contains the jdbc driver.

Under [/was-conf](https://github.com/cheeghi/websphere-setup/tree/main/was-conf) there are the jython scripts used to configure Websphere, you can look into them and add your own scripts to install new applications, add new datasources, change jvm properties, etc. If you install a new application, you must copy the war/ear into the container before, like [Dockerfile](https://github.com/cheeghi/websphere-setup/blob/main/Dockerfile) `COPY --chown=was:root webapp-1.0-SNAPSHOT.war /work`

## Oracle
Pretty much a default configuration of the [gvenzl/oracle-xe](https://github.com/gvenzl/oci-oracle-xe) image. You can connect to the database by:
```
jdbc: jdbc:oracle:thin:@//localhost:1521/XEPDB1
host: localhost
port: 1521
serviceName: XEPDB1
user: DEMO
password: DEMO
```
Setup sql must be placed under [/mount/sql](https://github.com/cheeghi/websphere-setup/tree/main/mount/sql).
