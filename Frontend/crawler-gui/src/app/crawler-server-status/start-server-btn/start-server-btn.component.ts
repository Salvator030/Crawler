import { Component, EventEmitter, Input, OnInit, Output } from '@angular/core';
import { CommonModule } from '@angular/common';
import { CrawlerServerStatusService } from '../crawler-server-status.service';
import { CrawlrBtnService } from './start-crawlr-btn.service';
import { SocketService } from '../../app-socket.service';

@Component({
  standalone: true,
  selector: 'app-start-server-btn',
  templateUrl: './start-server-btn.component.html',
  styleUrls: ['./start-server-btn.component.scss'],
  imports: [CommonModule]  // Importiere das CommonModule
})
export class StartServerBtnComponent implements OnInit {

  @Input()
  isCrawled!: boolean;
  
  @Output()
  isCrawledChange = new EventEmitter<boolean>
  
  btnText: string = ""
  restMsg: string = ""
  isDisabled: boolean = true;  // Statusvariable für den Button

  constructor(private statusService: CrawlerServerStatusService, private crawlerBtnService: CrawlrBtnService, private socket: SocketService) {}

  handelCrawlerBtn() {
    if (!this.isCrawled) {
      this.crawlerBtnService.startCrawler().subscribe({
        next: (response: any) => {
          if (response.msg == -1 ){
            this.restMsg = "crawler is not started"
             this.isCrawled = false;
             this.isCrawledChange.emit(this.isCrawled);
          }
          else if(response.msg == 1){
              this.isCrawled = true;
              this.isCrawledChange.emit(this.isCrawled);
              this.btnText = "stop"
          }
        }
      })
  
    } 
    else {
       this.crawlerBtnService.stopCrawler().subscribe({
        next: (response: any) => {
          if (response.msg == 1)
          this.restMsg = "crawler stopped after iteration";
          this.isDisabled = true
        }
      })

     }
  }

  ngOnInit() {
   if(!this.isCrawled){
    this.btnText = "start";
    this.isDisabled = false;
   }
   else{
    this.btnText = "stop";
    this.isDisabled = false;
   }


    // Höre auf das Event 'crawler_stopped'
    this.socket.fromEvent('crawler_stopped').subscribe((data: any) => {
      console.log(data.msg)
      this.btnText = "start"
      this.isDisabled = false; 
      this.restMsg = "" // Setze die Statusvariable zurück
      this.isCrawled = false
      this.isCrawledChange.emit(this.isCrawled);
    });
  }
}
