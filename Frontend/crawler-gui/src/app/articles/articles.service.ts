import { HttpClient } from '@angular/common/http';
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

}
