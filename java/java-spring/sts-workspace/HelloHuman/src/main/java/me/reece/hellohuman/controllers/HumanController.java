package me.reece.hellohuman.controllers;

import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class HumanController {
	@RequestMapping("/")
    public String index(
    		@RequestParam(name="firstName", required=false) String firstName,
    		@RequestParam(name="lastName", required=false) String lastName) {
        return "Hello " + firstName + " " + lastName;
    }
}
