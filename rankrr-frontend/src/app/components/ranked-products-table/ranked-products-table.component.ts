import { Component, Input, OnInit } from '@angular/core';

@Component({
  selector: 'app-ranked-products-table',
  templateUrl: './ranked-products-table.component.html',
  styleUrls: ['./ranked-products-table.component.css']
})
export class RankedProductsTableComponent implements OnInit {

  @Input() products: []

  constructor(){}

  ngOnInit(): void {
    
  }

}
