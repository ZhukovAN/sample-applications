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
    protected final String password = "%HuTt`3+9LnE~DMXLkdE";

    protected Connection connection;

    @SneakyThrows
    private Connection connect(final String url, final String user, final String pass) {
        return DriverManager.getConnection(url, user, pass);
    }

    protected Connection safeConnect() {
        return connect(
                System.getProperty("JDBC_URL"),
                System.getProperty("JDBC_USER"),
                System.getProperty("JDBC_PASSWORD"));
    }

    protected Connection unsafeConnect1() {
        return connect(
                "jdbc:mysql://mysql:3306/simple",
                "root", "cTW|C%;@$GM:^uk$a:zu");
    }

    protected Connection unsafeConnect2() {
        String innocentLookingVariable = "HBs72k;gq8VO?LAkOT1s";
        return connect(
                "jdbc:mysql://mysql:3306/simple",
                "root", innocentLookingVariable);
    }

    protected Connection unsafeConnect3() {
        String innocentLookingVariable = "KWem63?zl!YIt^c!c`Yi";
        String anotherInnocentLookingVariable = "DtN4X/y~AY;#'\\?#Xkj8";
        return connect(
                "jdbc:mysql://mysql:3306/simple",
                "root", innocentLookingVariable + anotherInnocentLookingVariable);
    }

    @Override
    public void init() {
        connection = safeConnect();
    }

    @Override
    protected void doGet(HttpServletRequest request,
                         HttpServletResponse response) {
    }
}
