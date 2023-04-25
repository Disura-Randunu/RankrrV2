import { Component } from '@angular/core';
import { RankerService } from 'src/app/services/ranker.service';
import { AgGridAngular } from 'ag-grid-angular';
import { CellClickedEvent, ColDef, GridReadyEvent } from 'ag-grid-community';
import { forkJoin } from 'rxjs';

@Component({
  selector: 'app-ranker',
  templateUrl: './ranker.component.html',
  styleUrls: ['./ranker.component.css'],
})
export class RankerComponent {
  
  products_with_extra = null;
  products_without_extra = null;

  product_id_column = 'product_id';
  review_text_column = 'review_body';
  max_products_amount = 15;
  file = null;

  file_name = null;

  rank_data_loading = false;
  sample_rank_data_loading = false

  loading_reviews_sentiments = false;
  reviews_sentiment_product_id = null;
  reviews_sentiments = null;
  reviews_sentiments_visible = false;

  constructor(private rankerService: RankerService) {
  }

  onChange(event) {
    this.file = event.target.files[0];
  }

  validateForm() {
    return this.file != null && this.product_id_column != '' && this.review_text_column != '' && this.max_products_amount != null;
  }

  onSubmit() {
    this.rank_data_loading = true;
    forkJoin([
      this.rankerService.rankCustomCSV(this.file, this.product_id_column, this.review_text_column, this.max_products_amount, true, true),
      this.rankerService.rankCustomCSV(this.file, this.product_id_column, this.review_text_column, this.max_products_amount, false, false),
    ]).subscribe(([data_with_extra, data_without_extra]) => {
      this.rank_data_loading = false;
      this.products_with_extra = data_with_extra.data;
      this.products_without_extra = data_without_extra.data;
      this.file_name = data_with_extra.file_name;
    })

  }

  showReviewsSentimentsDialog(product_id) {
    // this.reviews_sentiments_visible = true;
    this.loading_reviews_sentiments = true;
    this.reviews_sentiment_product_id = product_id;
    this.rankerService.getCustomCSVReviewsSentimentsForProduct(product_id, this.max_products_amount, this.file_name).subscribe((data) => {
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
