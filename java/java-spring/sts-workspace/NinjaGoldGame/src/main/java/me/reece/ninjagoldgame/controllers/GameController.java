package me.reece.ninjagoldgame.controllers;

import java.util.ArrayList;
import java.util.Date;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestParam;

import jakarta.servlet.http.HttpSession;

@Controller
public class GameController {

	@GetMapping("/")
	public String index(HttpSession session) {
		if(session.getAttribute("gold") == null) {
			session.setAttribute("gold", 0);
			session.setAttribute("activities", new ArrayList<>());
		}
		return "index.jsp";
	}
	
	@PostMapping("/findGold")
	public String findGold(
			@RequestParam("location") String location,
			HttpSession session
			) {
		int sessionGold = (int) session.getAttribute("gold");
		ArrayList<String> activities = (ArrayList<String>) session.getAttribute("activities");
		int goldEarned = 0;
		
		if(location.equals("farm")) {
			goldEarned = (int) (10 + Math.random() * 10);
		} else if(location.equals("cave")) {
			goldEarned = (int) (5 + Math.random() * 5);
		} else if(location.equals("house")) {
			goldEarned = (int) (2 + Math.random() * 3);
		} else if(location.equals("quest")) {
			goldEarned = (int) (Math.random() * 50);
		}

		session.setAttribute("gold", sessionGold + goldEarned);
		activities.add(String.format("You entered a %s and earned %s. (%s)", location, goldEarned, new Date()));
		
		return "redirect:/";
	}
	
}
