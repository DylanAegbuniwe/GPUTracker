import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-drop-box',
  templateUrl: './drop-box.component.html',
  styleUrls: ['./drop-box.component.css']
})
export class DropBoxComponent implements OnInit {
  names: string[] = ["Affogato",
  "Americano",
  "Bicerin",
  "Breve",
  "Café Bombón",
  "Café au lait",
  "Caffé Corretto",
  "Café Crema",
  "Caffé Latte",
  "Caffé macchiato",
  "Café mélange",
  "Coffee milk",
  "Cafe mocha",
  "Cappuccino",
  "Carajillo",
  "Cortado",
  "Cuban espresso",
  "Espresso",
  "Eiskaffee",
  "The Flat White",
  "Frappuccino",
  "Galao",
  "Greek frappé coffee",
  "Iced Coffee﻿",
  "Indian filter coffee",
  "Instant coffee",
  "Irish coffee",
  "Liqueur coffee"
];
  constructor() { }

  ngOnInit(): void {
  }

}
