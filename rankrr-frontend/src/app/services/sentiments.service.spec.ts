import { TestBed } from '@angular/core/testing';

import { SentimentsService } from './sentiments.service';

describe('SentimentsService', () => {
  let service: SentimentsService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(SentimentsService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
