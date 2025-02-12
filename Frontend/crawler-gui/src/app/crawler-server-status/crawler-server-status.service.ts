import { Injectable } from '@angular/core';
import { HttpClient } from "@angular/common/http";
import { Observable } from 'rxjs'

@Injectable({
  providedIn: 'root'
})
export class CrawlerServerStatusService {

  constructor(private http: HttpClient) { }
  
  getCrawlerServerStatus(): Observable<Object> {
    console.log("Requesting crawler status from server...");  // Debugging-Log
    return this.http.get("http://localhost:5000/crawler_status");
  }
}
