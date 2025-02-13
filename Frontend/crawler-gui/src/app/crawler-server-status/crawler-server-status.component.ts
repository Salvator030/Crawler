import { Component, OnInit } from '@angular/core';
import { CrawlerServerStatusService } from './crawler-server-status.service';
import { StartServerBtnComponent } from './start-server-btn/start-server-btn.component';
import { SocketService } from '../app-socket.service';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-crawler-server-status',
  templateUrl: './crawler-server-status.component.html',
  styleUrls: ['./crawler-server-status.component.scss'],
  standalone: true,
  imports: [StartServerBtnComponent,CommonModule]
})
export class CrawlerServerStatusComponent implements OnInit {

  isCrawled: boolean = false;
  status: string = ""

  constructor(private statusService: CrawlerServerStatusService, private socket: SocketService) {}


  ngOnInit(): void {
    this.statusService.getCrawlerServerStatus().subscribe({
      
      next: (response: any) => {
        console.log("response.msg: ", response.msg)
        if (response.msg == 1){
          this.isCrawled = true;
          this.status = "is running";  
        }
        else if (response.msg == 0){
          this.isCrawled = false;
          this.status = "is stopped"
        }
      },
      error: (error) => {
        console.error("Error fetching crawler status:", error);  // Debugging-Log
      }
    });

    this.socket.fromEvent('crawler_stopped').subscribe((data: any) => {
      this.isCrawled = false;
      // this.status = "is stopped";  // Setze die Statusvariable zurück
    });
  }

  updateStatus(isCrawled: boolean) {
    this.isCrawled = isCrawled;
    this.status = isCrawled ? "is running" : "is stopped";
  }

}
