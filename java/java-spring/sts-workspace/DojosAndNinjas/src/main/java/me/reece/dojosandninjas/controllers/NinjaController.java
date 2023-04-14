package me.reece.dojosandninjas.controllers;

import java.util.List;

import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.validation.BindingResult;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.ModelAttribute;
import org.springframework.web.bind.annotation.PostMapping;

import jakarta.validation.Valid;
import me.reece.dojosandninjas.models.Dojo;
import me.reece.dojosandninjas.models.Ninja;
import me.reece.dojosandninjas.services.DojoService;
import me.reece.dojosandninjas.services.NinjaService;

@Controller
public class NinjaController {
	private NinjaService ninjaService;
	private DojoService dojoService;
	
	public NinjaController(NinjaService ninjaService, DojoService dojoService) {
		this.ninjaService = ninjaService;
		this.dojoService = dojoService;
	}
	
	@GetMapping("/ninjas/new")
	public String ninjasNew(
			@ModelAttribute("ninja") Ninja ninja,
			Model model) {
		List<Dojo> dojos =  dojoService.findAll();
		model.addAttribute("dojos", dojos);
		return "/ninja/create.jsp";
	}
	
	@PostMapping("/ninjas/new")
	public String ninjasNewSubmit(
			@Valid @ModelAttribute("ninja") Ninja ninja,
			BindingResult result) {
		System.out.println(ninja.getDojo());
		if(result.hasErrors()) {
			return "/ninja/create.jsp";
		}
		ninjaService.create(ninja);
		return "redirect:/ninjas/new";
	}
}
