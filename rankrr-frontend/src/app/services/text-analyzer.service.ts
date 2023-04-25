import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';

const httpOptions = {
  headers: new HttpHeaders({
    'Content-Type': 'application/json'
  })
}

@Injectable({
  providedIn: 'root'
})
export class TextAnalyzerService {

  apiUrl = 'http://localhost:5000/text'

  constructor(private http: HttpClient) { }

  getAnalyzedText(text: string): Observable<any> {
    return this.http.post<any>(`${this.apiUrl}/analyze`, {text: text}, httpOptions)
  }

}
