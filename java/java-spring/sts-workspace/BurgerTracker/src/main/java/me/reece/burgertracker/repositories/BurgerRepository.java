package me.reece.burgertracker.repositories;

import java.util.List;

import org.springframework.data.repository.CrudRepository;
import org.springframework.stereotype.Repository;

import me.reece.burgertracker.models.Burger;

@Repository
public interface BurgerRepository extends CrudRepository<Burger, Long> {
	// get all
	List<Burger> findAll();
}

