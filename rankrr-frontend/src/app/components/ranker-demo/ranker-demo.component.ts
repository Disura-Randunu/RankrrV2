import { Component, OnInit } from '@angular/core';
import { forkJoin } from 'rxjs';
import { RankerService } from 'src/app/services/ranker.service';

@Component({
  selector: 'app-ranker-demo',
  templateUrl: './ranker-demo.component.html',
  styleUrls: ['./ranker-demo.component.css'],
})
export class RankerDemoComponent implements OnInit {
  products_with_extra = null;
  products_without_extra = null;
  loading_demo_data = false;

  reviews_sentiments_visible: boolean = false;
  reviews_sentiments: any[] = null;
  loading_reviews_sentiments: boolean = false;
  reviews_sentiment_product_id: string = null;

  constructor(private rankerService: RankerService) {}

  ngOnInit(): void {
    this.loading_demo_data = true;
    forkJoin([
      this.rankerService.getDemoRankedProducts(true, true),
      this.rankerService.getDemoRankedProducts(false, false),
    ]).subscribe(([products_with_extra, products_without_extra]) => {
      this.products_with_extra = products_with_extra.data;
      this.products_without_extra = products_without_extra.data;
      this.loading_demo_data = false;
    });
  }

  showReviewsSentimentsDialog(product_id) {
    // this.reviews_sentiments_visible = true;
    this.loading_reviews_sentiments = true;
    this.reviews_sentiment_product_id = product_id;
    this.rankerService.getDemoReviewsSentimentsForProduct(product_id).subscribe((data) => {
      this.reviews_sentiments = data.data;
      this.loading_reviews_sentiments = false;
    })
  }

  getRankChange(product_id){
    let product_with_extra = this.products_with_extra.find(product => product.product_id == product_id)
    let product_without_extra = this.products_without_extra.find(product => product.product_id == product_id)
    let rank_change = product_without_extra.rank - product_with_extra.rank
    return rank_change
  }

  getRankChangeColor(value){
    if(value > 0){
      return 'text-light bg-success'
    } else if(value < 0){
      return 'text-light bg-danger'
    } else {
      return ''
    }
  }
}
