package me.reece.burgertracker.services;

import java.util.List;
import java.util.Optional;

import org.springframework.stereotype.Service;

import me.reece.burgertracker.models.Burger;
import me.reece.burgertracker.repositories.BurgerRepository;

@Service
public class BurgerService {
	// adding the book repository as a dependency
    private final BurgerRepository burgerRepository;
    
    public BurgerService(BurgerRepository burgerRepository) {
        this.burgerRepository = burgerRepository;
    }
    
    // returns all the books
    public List<Burger> allBurgers() {
        return burgerRepository.findAll();
    }
    
    // creates a book
    public Burger createBurger(Burger b) {
        return burgerRepository.save(b);
    }
    
    // retrieves a book
    public Burger findBurger(Long id) {
        Optional<Burger> optionalBook = burgerRepository.findById(id);
        if(optionalBook.isPresent()) {
            return optionalBook.get();
        } else {
            return null;
        }
    }
    
    public Burger updateBurger(Long id, String name, String restaurantName, int rating, String notes) {
		Optional<Burger> optionalBurger = burgerRepository.findById(id);
		if(optionalBurger.isPresent()) {
			Burger burger = optionalBurger.get();
			burger.setId(id);
			burger.setName(name);
			burger.setRestaurantName(restaurantName);
			burger.setRating(rating);
			burger.setNotes(notes);
			return burgerRepository.save(burger);
		} else {
	    	return null;
		}
    }
    
    public void deleteBook(Long id) {
		Optional<Burger> optionalBurger = burgerRepository.findById(id);
		if(optionalBurger.isPresent()) {
			Burger burger = optionalBurger.get();
			burgerRepository.delete(burger);
		}
    }
}
