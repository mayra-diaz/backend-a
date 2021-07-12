package controller;

import business.UserService;
import data.dto.UserDTO;
import data.entities.User;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

import java.util.List;

import security.CurrentUser;
import security.UserPrincipal;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.security.access.prepost.PreAuthorize;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
@RequestMapping("/user")
public class UserController {

    @Autowired
    private UserService userService;

    @GetMapping("/user/me")
    @PreAuthorize("hasRole('USER')")
    public User getCurrentUser(@CurrentUser UserPrincipal userPrincipal) {
        return userService.findOneById(userPrincipal.getId());
    }


    @PostMapping
    @PreAuthorize("hasRole('USER')")
    public User postUser(@RequestBody UserDTO userDTO){
        return userService.saveUser(userDTO);
    }

    @GetMapping("/all")
    @PreAuthorize("hasRole('USER')")
    public List<User> listAllUsers(){
        return  userService.findAllUsers();
    }


    @PutMapping("/update/{area}/{id}")
    @PreAuthorize("hasRole('USER')")
    public void updateArea(@PathVariable String area, @PathVariable Long id){
        userService.updateUser(area, id);
    }

    @GetMapping("/get/{id}")
    @PreAuthorize("hasRole('USER')")
    public User getUserById(@PathVariable Long id) {
        return userService.findOneById(id);
    }

    @DeleteMapping("/delete/{id}")
    @PreAuthorize("hasRole('USER')")
    public void deleteUserById(@PathVariable Long id){
        userService.eraseUserById(id) ;
    }




}
