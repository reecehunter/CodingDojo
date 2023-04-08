package me.reece.daikichiroutes.controllers;

import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class DaikichiControllers {
	
	@RequestMapping("/daikichi")
	public String daikichi() {
		return "Welcome!";
	}
	
	@RequestMapping("/daikichi/today")
	public String daikichiToday() {
		return "Today you will find luck in all your endeavors!";
	}
	
	@RequestMapping("/daikichi/tomorrow")
	public String daikichiTomorrow() {
		return "Tomorrow, an opportunity will arise, so be sure to be open to new ideas!";
	}

}
