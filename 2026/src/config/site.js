// Central site configuration — reads PUBLIC_ environment variables available at build/runtime
export const registrationSite = (
  typeof import.meta !== 'undefined' && import.meta.env && import.meta.env.PUBLIC_REGISTRATION_SITE
) ? import.meta.env.PUBLIC_REGISTRATION_SITE : '';

export const contactEmail = (
  typeof import.meta !== 'undefined' && import.meta.env && import.meta.env.PUBLIC_CONTACT_EMAIL
) ? import.meta.env.PUBLIC_CONTACT_EMAIL : '';

export const cfpFormUrl = (
  typeof import.meta !== 'undefined' && import.meta.env && import.meta.env.PUBLIC_CFP_FORM_URL
) ? import.meta.env.PUBLIC_CFP_FORM_URL : '';

export const communityPrioritiesUrl = 'https://inguandes.typeform.com/jccs-2026-pe?utm_source=web_jccs&utm_medium=homepage&utm_campaign=prioridades_2026_2027';

export default {
  cfpFormUrl,
  communityPrioritiesUrl,
  contactEmail,
  registrationSite,
};
