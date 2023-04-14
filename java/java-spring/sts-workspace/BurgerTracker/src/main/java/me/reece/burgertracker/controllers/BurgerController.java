package me.reece.burgertracker.controllers;

import java.util.List;

import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.validation.BindingResult;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.ModelAttribute;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;

import jakarta.validation.Valid;
import me.reece.burgertracker.models.Burger;
import me.reece.burgertracker.services.BurgerService;


@Controller
public class BurgerController {
	private BurgerService burgerService;
	
	public BurgerController(BurgerService burgerService) {
		this.burgerService = burgerService;
	}

	@GetMapping("/")
	public String index(
			@ModelAttribute("burger") Burger burger,
			Model model) {
		List<Burger> burgers = burgerService.allBurgers();
		model.addAttribute("burgers", burgers);
		return "index.jsp";
	}
	
	@PostMapping("/burgers/new")
	public String burgerCreate(
			@Valid @ModelAttribute("burger") Burger burger,
			BindingResult result) {
		if(result.hasErrors()) {
			return "index.jsp";
		}
		burgerService.createBurger(burger);
		return "redirect:/";
	}
	
	@GetMapping("/burgers/edit/{id}")
	public String burgerEdit(
			@PathVariable("id") Long id,
			Model model) {
		Burger burger = burgerService.findBurger(id);
		model.addAttribute("burger", burger);
		return "/burger/edit.jsp";
	}
	
	@PostMapping("/burgers/{id}")
	public String burgerEditSubmit(
			@PathVariable("id") Long id,
			Model model,
			@Valid @ModelAttribute("burger") Burger burger,
			BindingResult result) {
		if(result.hasErrors()) {
			return "/burger/edit.jsp";
		}
		burgerService.updateBurger(burger);
		return "redirect:/";
	}

}
