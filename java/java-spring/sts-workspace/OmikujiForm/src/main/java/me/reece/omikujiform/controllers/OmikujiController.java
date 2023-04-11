package me.reece.omikujiform.controllers;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestParam;

import jakarta.servlet.http.HttpSession;

@Controller
public class OmikujiController {
	
	@GetMapping("/")
	public String index() {
		return "index.jsp";
	}
	
	@PostMapping("/send")
	public String send(
			@RequestParam(value="amount") int amount,
			@RequestParam(value="cityName") String cityName,
			@RequestParam(value="personName") String personName,
			@RequestParam(value="hobby") String hobby,
			@RequestParam(value="livingThing") String livingThing,
			@RequestParam(value="nice") String nice,
			HttpSession session
			) {
		session.setAttribute("amount", amount);
		session.setAttribute("cityName", cityName);
		session.setAttribute("personName", personName);
		session.setAttribute("hobby", hobby);
		session.setAttribute("livingThing", livingThing);
		session.setAttribute("nice", nice);
		return "redirect:/show";
	}
	
	@GetMapping("/show")
	public String show() {
		return "show.jsp";
	}

}
