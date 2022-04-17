package com.github.cheeghi;

import javax.annotation.Resource;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.sql.DataSource;
import java.io.IOException;
import java.sql.Connection;
import java.sql.SQLException;
import java.sql.Statement;
import java.util.Properties;

@WebServlet("/probe")
public class ProbeServlet extends HttpServlet {

    @Resource(name = "default/ds")
    private DataSource dataSource;

    @Override
    protected void doGet(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {
        probeDatabaseConnection();
        probeSharedLib();
        resp.getWriter().println("Ok");
    }

    private void probeDatabaseConnection() {
        try (Connection connection = dataSource.getConnection()) {
            Statement stmt = connection.createStatement();
            stmt.execute("select * from DUMMY");
        } catch (SQLException e) {
            throw new RuntimeException("Failed to probe database connection", e);
        }
    }

    private void probeSharedLib() throws IOException {
        Properties applicationProperties = loadApplicationProperties();
        String probe = applicationProperties.getProperty("probe");
        if (!"cheeghi".equals(probe)) {
            throw new IllegalStateException("Failed to probe shared lib");
        }
    }

    private Properties loadApplicationProperties() throws IOException {
        Properties properties = new Properties();
        properties.load(getClass().getClassLoader().getResourceAsStream("application.properties"));
        return properties;
    }

}
