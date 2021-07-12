package enrollment.projection.enrollmentprojection;

import config.AppProperties;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.boot.context.properties.EnableConfigurationProperties;

@SpringBootApplication
@EnableConfigurationProperties(AppProperties.class)
public class EnrollmentProjectionApplication {

    public static void main(String[] args) {
        SpringApplication.run(EnrollmentProjectionApplication.class, args);
    }

}
