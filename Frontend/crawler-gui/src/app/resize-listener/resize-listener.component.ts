import { Component, HostListener, OnInit, Renderer2 } from '@angular/core';

@Component({
  selector: 'app-resize-listener',
  imports: [],
  templateUrl: './resize-listener.component.html',
  styleUrl: './resize-listener.component.scss'
})
export class ResizeListenerComponent implements OnInit {

  // Variable zur Speicherung der Fenstergröße
  screenWidth: number = 0;
  screenHeight: number = 0;

  constructor(private renderer: Renderer2) {}

  ngOnInit() {
    // Initiale Fenstergröße erfassen
    this.screenWidth = window.innerWidth;
    this.screenHeight = window.innerHeight;
    this.setAppSize();
  }

  @HostListener('window:resize', ['$event'])
  onResize(event: any) {
    // Aktualisieren der Fenstergröße bei Änderung
    this.screenWidth = event.target.innerWidth;
    this.screenHeight = event.target.innerHeight;
    this.setAppSize();
  }

  setAppSize() {
    // Anpassen der App-Größe basierend auf der Fenstergröße
    this.renderer.setStyle(document.body, 'width', `${this.screenWidth}px`);
    this.renderer.setStyle(document.body, 'height', `${this.screenHeight}px`);
  }
}