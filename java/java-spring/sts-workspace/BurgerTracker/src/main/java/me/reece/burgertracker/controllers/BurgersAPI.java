package me.reece.burgertracker.controllers;

import org.springframework.web.bind.annotation.DeleteMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PutMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

import me.reece.burgertracker.models.Burger;
import me.reece.burgertracker.services.BurgerService;

@RestController
public class BurgersAPI {
    private final BurgerService burgerService;
    
    public BurgersAPI(BurgerService burgerService){
        this.burgerService = burgerService;
    }
    
    // Update
    @PutMapping(value="/api/burgers/{id}")
    public Burger update(
    		@PathVariable("id") Long id, 
    		@RequestParam(value="name") String name, 
    		@RequestParam(value="restaurantName") String restaurantName, 
    		@RequestParam(value="rating") Integer rating,
    		@RequestParam(value="notes") String notes) {
    	Burger burger = burgerService.updateBurger(id, name, restaurantName, rating, notes);
        return burger;
    }
    
    // Delete
    @DeleteMapping(value="/api/burgers/{id}")
    public void destroy(@PathVariable("id") Long id) {
    	burgerService.deleteBook(id);
    }
}
