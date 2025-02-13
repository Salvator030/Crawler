import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class ArticlesService {

  constructor(private http: HttpClient) {}

  getAllArticles(): Observable<Object>{
    console.log("Requesting allArticles...");  // Debugging-Log
    return this.http.get("http://localhost:5000/all_articles");
  }

  getArticlesBy(data: any): Observable<any> {
    const headers = new HttpHeaders({ 'Content-Type': 'application/json' });
    return this.http.post<any>("http://localhost:5000/articles_by", data, { headers });
}
}