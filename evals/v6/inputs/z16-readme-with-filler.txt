## Calibrating the spindle scanner

Following these steps carefully is very important for a good result.

1. Power off the Sample Mill scanner and wait 30 seconds.
2. Remove the cover plate with a 3 mm hex key. Keep all four screws.
3. Hold the reference bar (part RB-12) against the left rail and tighten the clamp to 2 Nm.
4. Run `./calibrate.sh --axis x --samples 50` from the tools folder. It takes about 6 minutes.
5. If the reported offset is above 0.05 mm, loosen the clamp, move the bar 1 mm toward the rail and repeat step 4.
6. When the offset is 0.05 mm or lower, copy `calib_x.json` to `/etc/spindle/` and restart the service with `sudo systemctl restart spindled`.
7. Refit the cover plate. Do not tighten the screws beyond 1.5 Nm.
