import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs/internal/Observable';

@Injectable({
  providedIn: 'root'
})
export class CrawlrBtnService {

  constructor(private http: HttpClient) { }

  startCrawler():  Observable<Object> {
      console.log("Requesting startCrawler from server...");  // Debugging-Log
      return this.http.get("http://localhost:5000/start_crawler");
    }

  stopCrawler():  Observable<Object> {
    console.log("Requesting stopCrawler from server...");  // Debugging-Log
    return this.http.get("http://localhost:5000/stop_crawler");
  }
}
