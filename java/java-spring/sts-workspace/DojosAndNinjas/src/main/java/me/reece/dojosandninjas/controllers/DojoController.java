package me.reece.dojosandninjas.controllers;

import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.validation.BindingResult;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.ModelAttribute;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;

import jakarta.validation.Valid;
import me.reece.dojosandninjas.models.Dojo;
import me.reece.dojosandninjas.services.DojoService;

@Controller
public class DojoController {
	
	private DojoService dojoService;
	
	public DojoController(DojoService dojoService) {
		this.dojoService = dojoService;
	}
	
	@GetMapping("/dojos/{id}")
	public String dojoShowOne(
			@PathVariable("id") Long id,
			Model model) {
		Dojo dojo = dojoService.findOne(id);
		model.addAttribute("dojo", dojo);
		return "/dojo/showOne.jsp";
	}
	
	@GetMapping("/dojos/new")
	public String dojoNew(@ModelAttribute("dojo") Dojo dojo) {
		return "/dojo/create.jsp";
	}
	
	@PostMapping("/dojos/new")
	public String dojoNewSubmit(
			@Valid @ModelAttribute("dojo") Dojo dojo,
			BindingResult result) {
		if(result.hasErrors()) {
			return "/dojo/create.jsp";
		}
		dojoService.create(dojo);
		return "redirect:/dojos/new";
	}

}
