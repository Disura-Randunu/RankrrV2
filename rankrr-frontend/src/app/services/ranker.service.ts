import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';

const httpOptions = {
  headers: new HttpHeaders({
    'Content-Type': 'application/json',
  }),
};

@Injectable({
  providedIn: 'root',
})
export class RankerService {
  apiUrl = 'http://localhost:5000/ranker';

  constructor(private http: HttpClient) {}

  getAnalyzedText(text: string): Observable<any> {
    return this.http.post<any>(
      `${this.apiUrl}/analyze`,
      { text: text },
      httpOptions
    );
  }

  getDemoRankedProducts(consider_emoji: boolean, consider_emphasized_text: boolean): Observable<any>{
    let consider_emoji_query_value = consider_emoji ? 'true' : 'false'
    return this.http.post<any>(`${this.apiUrl}/demo`, {
      consider_emoji: consider_emoji, 
      consider_emphasized_text: consider_emphasized_text
    }, httpOptions)
  }

  getDemoReviewsSentimentsForProduct(product_id): Observable<any>{
    return this.http.post<any>(`${this.apiUrl}/demo/${product_id}/reviews/sentiments`, {},  httpOptions)
  }

  getCustomCSVReviewsSentimentsForProduct(product_id, max_products_amount, file_name): Observable<any>{
    return this.http.post<any>(`${this.apiUrl}/custom-csv/${product_id}/reviews/sentiments`, {
      max_products_amount: max_products_amount,
      file_name: file_name
    }, httpOptions)
  }


  rankCustomCSV(file, product_id_column, review_text_column, max_products_amount, consider_emoji, consider_emph_text): Observable<any> {
    const formData = new FormData();

    formData.append('csv_file', file, file.name);
    formData.append('product_id_column', product_id_column);
    formData.append('review_text_column', review_text_column);
    formData.append('max_products_amount', max_products_amount);
    formData.append('consider_emoji', consider_emoji ? '1' : '0');
    formData.append('consider_emph_text', consider_emph_text ? '1' : '0');

    return this.http.post<any>(`${this.apiUrl}/process-csv`, formData);
  }
}
