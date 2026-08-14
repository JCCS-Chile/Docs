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

export default {
  cfpFormUrl,
  contactEmail,
  registrationSite,
};
