package controller;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

import java.security.Principal;


@RestController
public class AppController {

    @GetMapping
    public String welcome(){
        return "Welcome!";
    }

    @GetMapping("/prueba")
    public Principal user_(Principal principal){
        System.out.println("username: "+ principal.getName());
        return  principal;
    }


}
