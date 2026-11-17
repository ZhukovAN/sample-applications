package local.ptdemo.appsec.poc.servlet.simple;

import lombok.SneakyThrows;

import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.sql.Connection;
import java.sql.DriverManager;

@WebServlet("/simple")
public class Servlet extends HttpServlet {
    protected Connection connection;

    @Override
    public void init() {
        if (true) {
            connection = DriverManager.getConnection(
                System.getProperty("JDBC_URL"),
                System.getProperty("JDBC_USER"),
                System.getProperty("JDBC_PASSWORD"));
        }
    }

    @Override
    protected void doGet(HttpServletRequest request,
                         HttpServletResponse response) {
    }
}
