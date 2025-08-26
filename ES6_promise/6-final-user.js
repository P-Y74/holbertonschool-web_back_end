import signUpUser from './4-user-promise';
import uploadPhoto from './5-photo-reject';

export default function handleProfileSignup(firstName, lastName, fileName) {
  return Promise.allSettled([signUpUser(firstName, lastName), uploadPhoto(fileName)])
    .then(result =>
      result.map(r => r.status === 'fulfilled' ? r : { status: r.status, value: r.reason.toString() })
    );
}
