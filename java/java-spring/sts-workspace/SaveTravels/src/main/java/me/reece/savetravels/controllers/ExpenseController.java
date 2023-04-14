package me.reece.savetravels.controllers;

import java.util.List;

import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.validation.BindingResult;
import org.springframework.web.bind.annotation.DeleteMapping;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.ModelAttribute;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;

import jakarta.validation.Valid;
import me.reece.savetravels.models.Expense;
import me.reece.savetravels.services.ExpenseService;


@Controller
public class ExpenseController {
	private ExpenseService service;
	
	public ExpenseController(ExpenseService service) {
		this.service = service;
	}

	@GetMapping("/expenses")
	public String index(
			@ModelAttribute("expense") Expense burger,
			Model model) {
		List<Expense> expenses = service.findAll();
		model.addAttribute("expenses", expenses);
		return "index.jsp";
	}

	@GetMapping("/expenses/{id}")
	public String showOne(
			@PathVariable("id") Long id,
			@ModelAttribute("expense") Expense burger,
			Model model) {
		Expense expense = service.findOne(id);
		model.addAttribute("expense", expense);
		return "showOne.jsp";
	}
	
	@PostMapping("/expenses/new")
	public String expenseCreate(
			@Valid @ModelAttribute("expense") Expense expense,
			BindingResult result) {
		if(result.hasErrors()) {
			return "index.jsp";
		}
		service.create(expense);
		return "redirect:/expenses";
	}
	
	@GetMapping("/expenses/edit/{id}")
	public String expenseEdit(
			@PathVariable("id") Long id,
			Model model) {
		Expense expense = service.findOne(id);
		model.addAttribute("expense", expense);
		return "/edit.jsp";
	}
	
	@PostMapping("/expenses/{id}")
	public String expenseEditSubmit(
			@PathVariable("id") Long id,
			Model model,
			@Valid @ModelAttribute("expense") Expense expense,
			BindingResult result) {
		if(result.hasErrors()) {
			return "/edit.jsp";
		}
		service.update(expense);
		return "redirect:/expenses";
	}
	
	@PostMapping("/expenses/delete/{id}")
	public String delete(@PathVariable("id") Long id) {
		service.delete(id);
		return "redirect:/expenses";
	}

}
