package me.reece.loginandregistration.controllers;

import java.util.List;

import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.validation.BindingResult;
import org.springframework.web.bind.annotation.DeleteMapping;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.ModelAttribute;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestMapping;

import jakarta.servlet.http.HttpSession;
import jakarta.validation.Valid;
import me.reece.loginandregistration.models.Book;
import me.reece.loginandregistration.models.LoginUser;
import me.reece.loginandregistration.models.User;
import me.reece.loginandregistration.models.ValidateBook;
import me.reece.loginandregistration.services.BookService;
import me.reece.loginandregistration.services.UserService;

@Controller
@RequestMapping("/books")
public class BookController {
	private final BookService bookService;
	private final UserService userService;
	
	public BookController(BookService bookService, UserService userService) {
		this.bookService = bookService;
		this.userService = userService;
	}
	
	@GetMapping("")
	public String showAll(Model model, HttpSession session) {
		if(session.getAttribute("user_id") == null) {
			return "redirect:/users";
		}
		final long id = (long) session.getAttribute("user_id");
		User user = userService.getUser(id);
		model.addAttribute("user", user);
		
		List<Book> books = bookService.getAll();
		model.addAttribute("books", books);
		return "/book/showAll.jsp";
	}
	
	@GetMapping("/{id}")
	public String showOne(
			@PathVariable("id") long id,
			Model model) {
		Book book = bookService.getOne(id);
		model.addAttribute("book", book);
		return "/book/showOne.jsp";
	}
	
	@GetMapping("/new")
	public String newBook(
			@ModelAttribute("newBook") Book book,
			@ModelAttribute("validateBook") LoginUser loginUser,
			Model model,
			HttpSession session) {
		if(session.getAttribute("user_id") == null) {
			return "redirect:/users";
		}
		final long id = (long) session.getAttribute("user_id");
		User user = userService.getUser(id);
		model.addAttribute("user", user);
		return "/book/new.jsp";
	}
	
	@PostMapping("/process/new")
	public String processNewBook(
			@Valid @ModelAttribute("newBook") Book book,
			BindingResult result,
			Model model,
			HttpSession session) {
		// re-render if errors
		if(result.hasErrors()) {
			model.addAttribute("validateBook", new ValidateBook());
			return "/book/new.jsp";
		}
		
		Book newBook = bookService.createOne(book);
		return "redirect:/books/"+newBook.getId();
	}
	
	@GetMapping("/edit/{id}")
	public String editOne(
			@ModelAttribute("newBook") Book newBook,
			@ModelAttribute("validateBook") ValidateBook validateBook,
			@PathVariable("id") long id,
			Model model) {
		Book book = bookService.getOne(id);
		model.addAttribute("book", book);
		return "/book/edit.jsp";
	}
	
	@PostMapping("/process/edit/{id}")
	public String processEditOne(
			@PathVariable("id") long id,
			@Valid @ModelAttribute("newBook") Book book,
			BindingResult result,
			Model model,
			HttpSession session) {
		if(result.hasErrors()) {
			model.addAttribute("book", book);
			return "/book/edit.jsp";
		}
		bookService.update(book);
		return "redirect:/books/" + id;
	}
	
	@DeleteMapping("/delete/{id}")
	public String delete(@PathVariable("id") Long id) {
		bookService.delete(id);
		return "redirect:/books";
	}

}
