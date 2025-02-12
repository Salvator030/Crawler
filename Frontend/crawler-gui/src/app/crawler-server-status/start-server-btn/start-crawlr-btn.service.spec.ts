import { TestBed } from '@angular/core/testing';

import { StartCrawlrBtnService } from './start-crawlr-btn.service';

describe('StartCrawlrBtnService', () => {
  let service: StartCrawlrBtnService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(StartCrawlrBtnService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
