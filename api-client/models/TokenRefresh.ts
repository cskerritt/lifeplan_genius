/* tslint:disable */
/* eslint-disable */
/**
 * Lifeplan Genius
 * LCP Tool for KW
 *
 * The version of the OpenAPI document: 0.1.0
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

import { mapValues } from '../runtime';
/**
 * 
 * @export
 * @interface TokenRefresh
 */
export interface TokenRefresh {
    /**
     * 
     * @type {string}
     * @memberof TokenRefresh
     */
    readonly access: string;
    /**
     * 
     * @type {string}
     * @memberof TokenRefresh
     */
    refresh: string;
}

/**
 * Check if a given object implements the TokenRefresh interface.
 */
export function instanceOfTokenRefresh(value: object): value is TokenRefresh {
    if (!('access' in value) || value['access'] === undefined) return false;
    if (!('refresh' in value) || value['refresh'] === undefined) return false;
    return true;
}

export function TokenRefreshFromJSON(json: any): TokenRefresh {
    return TokenRefreshFromJSONTyped(json, false);
}

export function TokenRefreshFromJSONTyped(json: any, ignoreDiscriminator: boolean): TokenRefresh {
    if (json == null) {
        return json;
    }
    return {
        
        'access': json['access'],
        'refresh': json['refresh'],
    };
}

  export function TokenRefreshToJSON(json: any): TokenRefresh {
      return TokenRefreshToJSONTyped(json, false);
  }

  export function TokenRefreshToJSONTyped(value?: Omit<TokenRefresh, 'access'> | null, ignoreDiscriminator: boolean = false): any {
    if (value == null) {
        return value;
    }

    return {
        
        'refresh': value['refresh'],
    };
}

