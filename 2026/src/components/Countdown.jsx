import { useEffect } from "react";

const SECOND = 1000;
const MINUTE = 60 * SECOND;
const HOUR = 60 * MINUTE;
const DAY = 24 * HOUR;

function formatTimeLeft(targetDate) {
  const remaining = Math.max(targetDate.getTime() - Date.now(), 0);

  return {
    days: Math.floor(remaining / DAY),
    hours: Math.floor((remaining % DAY) / HOUR),
    minutes: Math.floor((remaining % HOUR) / MINUTE),
    seconds: Math.floor((remaining % MINUTE) / SECOND),
  };
}

function padUnit(unit, value) {
  return String(value).padStart(unit === "days" ? 3 : 2, "0");
}

export default function Countdown() {
  useEffect(() => {
    const countdowns = Array.from(document.querySelectorAll("[data-countdown-target]"));
    if (!countdowns.length) {
      return undefined;
    }

    const updateCountdowns = () => {
      countdowns.forEach((countdown) => {
        const target = new Date(countdown.dataset.countdownTarget);
        const timeLeft = formatTimeLeft(target);

        Object.entries(timeLeft).forEach(([unit, value]) => {
          const element = countdown.querySelector(`[data-countdown-unit="${unit}"]`);
          if (element) {
            element.textContent = padUnit(unit, value);
          }
        });
      });
    };

    updateCountdowns();
    const interval = window.setInterval(updateCountdowns, SECOND);

    return () => window.clearInterval(interval);
  }, []);

  return null;
}
