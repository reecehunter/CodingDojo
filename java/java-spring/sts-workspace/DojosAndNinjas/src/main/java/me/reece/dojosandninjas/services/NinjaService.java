package me.reece.dojosandninjas.services;

import java.util.List;
import java.util.Optional;

import org.springframework.stereotype.Service;

import me.reece.dojosandninjas.models.Ninja;
import me.reece.dojosandninjas.repositories.NinjaRepository;

@Service
public class NinjaService {
	// adding the book repository as a dependency
    private final NinjaRepository repo;
    
    public NinjaService(NinjaRepository repo) {
        this.repo = repo;
    }
    
    // returns all the books
    public List<Ninja> findAll() {
        return repo.findAll();
    }
    
    // creates a book
    public Ninja create(Ninja b) {
        return repo.save(b);
    }
    
    // retrieves a book
    public Ninja findOne(Long id) {
        Optional<Ninja> optional = repo.findById(id);
        if(optional.isPresent()) {
            return optional.get();
        } else {
            return null;
        }
    }
    
    public Ninja update(Ninja newObj) {
		Optional<Ninja> optional = repo.findById(newObj.getId());
		if(optional.isPresent()) {
			return repo.save(newObj);
		} else {
	    	return null;
		}
    }
    
    public void delete(Long id) {
		Optional<Ninja> optional = repo.findById(id);
		if(optional.isPresent()) {
			Ninja obj = optional.get();
			repo.delete(obj);
		}
    }
}
