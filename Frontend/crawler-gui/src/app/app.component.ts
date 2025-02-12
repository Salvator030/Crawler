import { Component } from '@angular/core';
import { CrawlerServerStatusComponent } from './crawler-server-status/crawler-server-status.component';
import { StartServerBtnComponent } from './crawler-server-status/start-server-btn/start-server-btn.component';

@Component({
  selector: 'app-root',
  imports: [CrawlerServerStatusComponent],
  templateUrl: './app.component.html',
  styleUrl: './app.component.scss'
})
export class AppComponent {
  title = 'crawler-gui';
}
 