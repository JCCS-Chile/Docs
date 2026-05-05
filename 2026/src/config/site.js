// Central site configuration — reads PUBLIC_ environment variables available at build/runtime
export const registrationSite = (
  typeof import.meta !== 'undefined' && import.meta.env && import.meta.env.PUBLIC_REGISTRATION_SITE
) ? import.meta.env.PUBLIC_REGISTRATION_SITE : '';

export default {
  registrationSite,
};
