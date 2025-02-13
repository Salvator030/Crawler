import { ComponentFixture, TestBed } from '@angular/core/testing';

import { CrawlerServerStatusComponent } from './crawler-server-status.component';

describe('CrawlerServerStatusComponent', () => {
  let component: CrawlerServerStatusComponent;
  let fixture: ComponentFixture<CrawlerServerStatusComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [CrawlerServerStatusComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(CrawlerServerStatusComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
