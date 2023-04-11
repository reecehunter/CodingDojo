package me.reece.counter.controllers;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;

import jakarta.servlet.http.HttpSession;

@Controller
public class CounterController {
	
	@GetMapping("/")
	public String index(HttpSession session) {
		if(session.getAttribute("count") == null) {
			session.setAttribute("count", 0);
		}
		
		int countFromSession = (int) session.getAttribute("count");
		session.setAttribute("count", countFromSession + 1);
		
		return "index.jsp";
	}
	
	@GetMapping("/counter")
	public String counter(HttpSession session) {
		if(session.getAttribute("count") == null) {
			session.setAttribute("count", 0);
		}
		
		return "counter.jsp";
	}

}
