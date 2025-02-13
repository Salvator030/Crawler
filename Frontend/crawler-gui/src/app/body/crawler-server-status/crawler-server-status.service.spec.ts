import { TestBed } from '@angular/core/testing';

import { CrawlerServerStatusService } from './crawler-server-status.service';

describe('CrawlerServerStatusService', () => {
  let service: CrawlerServerStatusService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(CrawlerServerStatusService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
